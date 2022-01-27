import pandas as pd
from tensorflow.keras.utils import to_categorical
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input, Dense
from transformers import AutoTokenizer,TFBertModel


def prepare_model():
    df=pd.read_csv('cars.csv')
    df.head()

    y_train = to_categorical(df.category_1)
    y_test = to_categorical(df.category_1)

    tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
    bert = TFBertModel.from_pretrained('bert-base-cased')

    # here tokenizer using from bert-base-cased
    x_train = tokenizer(
        text=df.text.tolist(),
        add_special_tokens=True,
        max_length=70,
        truncation=True,
        padding=True, 
        return_tensors='tf',
        return_token_type_ids = False,
        return_attention_mask = True,
        verbose = True)

    x_test = tokenizer(
        text=df.text.tolist(),
        add_special_tokens=True,
        max_length=70,
        truncation=True,
        padding=True, 
        return_tensors='tf',
        return_token_type_ids = False,
        return_attention_mask = True,
        verbose = True)


    input_ids = x_train['input_ids']
    attention_mask = x_train['attention_mask']


    max_len = 12
    input_ids = Input(shape=(max_len,), dtype=tf.int32, name="input_ids")
    input_mask = Input(shape=(max_len,), dtype=tf.int32, name="attention_mask")
    embeddings = bert(input_ids,attention_mask = input_mask)[0] 
    out = tf.keras.layers.GlobalMaxPool1D()(embeddings)
    out = Dense(128, activation='relu')(out)
    out = tf.keras.layers.Dropout(0.1)(out)
    out = Dense(32,activation = 'relu')(out)    
    y = Dense(3,activation = 'sigmoid')(out)
    model = tf.keras.Model(inputs=[input_ids, input_mask], outputs=y)

    model.layers[2].trainable = True

    optimizer = Adam(
        learning_rate=5e-05, 
        epsilon=1e-08,
        decay=0.01,
        clipnorm=1.0)
    # Set loss and metrics
    loss =CategoricalCrossentropy(from_logits = True)
    metric = CategoricalAccuracy('balanced_accuracy'),
    # Compile the model
    model.compile(
        optimizer = optimizer,
        loss = loss, 
        metrics = metric)

    train_history = model.fit(
        x ={'input_ids':x_train['input_ids'],'attention_mask':x_train['attention_mask']} ,
        y = y_train,
        validation_data = (
        {'input_ids':x_test['input_ids'],'attention_mask':x_test['attention_mask']}, y_test
        ),
    epochs=1,
        batch_size=36
    )

    return model

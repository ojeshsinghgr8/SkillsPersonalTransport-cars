

from transformers import AutoTokenizer,TFBertModel
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from init_model import prepare_model

tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
bert = TFBertModel.from_pretrained('bert-base-cased')


new_model =  prepare_model()

texts = input(str('input the text'))
x_val = tokenizer(
    text=texts,
    add_special_tokens=True,
    max_length=12,
    truncation=True,
    padding='max_length', 
    return_tensors='tf',
    return_token_type_ids = False,
    return_attention_mask = True,
    verbose = True) 
validation = new_model.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})*100
print(validation)
from asyncio.windows_events import NULL
from df_engine.core import Context, Actor
import re
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
prepModel=NULL

def is_car_service(ctx: Context, actor: Actor, *args, **kwargs) -> bool:
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=12,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})*100          
        return max(validation[0])>50 and validation[0][0]==max(validation[0])
    else:
        return False

def is_road_assistance(ctx: Context, actor: Actor, *args, **kwargs) -> bool:    
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=12,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})*100    
        
        return max(validation[0])>50 and validation[0][1]==max(validation[0])
    else:
        return False

def is_book_car(ctx: Context, actor: Actor, *args, **kwargs) -> bool:    
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=12,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})*100            
        return  max(validation[0])>50 and validation[0][2]==max(validation[0])
    else:
        return False    

def is_fallback(ctx: Context, actor: Actor, *args, **kwargs) -> bool:    
    if prepModel:
        x_val = tokenizer(
            text=ctx.last_request,
            add_special_tokens=True,
            max_length=12,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True) 
        validation = prepModel.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})*100    
           
        return  max(validation[0])<=50
    else:
        return False        
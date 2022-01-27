from df_engine.core import Actor
from df_engine.core.keywords import RESPONSE
from df_engine.core.keywords import GLOBAL,TRANSITIONS, RESPONSE
import re
import df_engine.conditions as cnd
import scenario.condition as cust_cnd
plot = {
    "global": {
        "start": {
            RESPONSE: "",
            TRANSITIONS: {
                "intro": cnd.regexp(r"hi|hello", re.IGNORECASE),
            }
        },
        "intro": {
            RESPONSE: "Welcome, to our Car service catbot.\n We provide following services \n 1. Renting \n 2. Roadside Assistance \n 3. Maintenance".format(), 
            TRANSITIONS: {
                ("car_rental", "start"): cust_cnd.is_book_car,
                ("road_assistance", "start"): cust_cnd.is_road_assistance,
                ("car_service", "start"): cust_cnd.is_car_service,
                ("global", "fallback"): cust_cnd.is_fallback,
            }
        },     
        "fallback": {
            RESPONSE: "Oops!! something went wrong. Lets start again...",
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }
        }
    },
    "car_rental":{
        "start":{
            RESPONSE: "Welcome, to our Rental service.\n What type of car you want to rent \n 1. SUV \n 2. Sedan".format(), 
            TRANSITIONS: {
                    ("suv","start"): cnd.regexp(r".*(suv|1)", re.IGNORECASE),
                    ("sedan","start"): cnd.regexp(r".*(sedan|2)", re.IGNORECASE),                    
                }
        },
        "book_success":{
            RESPONSE: "Your booking have been completed." .format(), 
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }
    },
    },
    "suv":{
        "start":{
            RESPONSE: "Great, we have following SUV \n 1. Honda Pilot   $100/day \n 2. Toyota Fortuner   $80/day \n 3. Renault Duster    $50/day \n Please, enter your selection number" .format(), 
            TRANSITIONS: {
                    ("suv","car1"): cnd.regexp(r".*(Honda|Pilot|Honda Pilot|1)", re.IGNORECASE),
                    ("suv","car2"): cnd.regexp(r".*(Toyota|Fortuner|Toyota Fortuner|2)", re.IGNORECASE),
                    ("suv","car3"): cnd.regexp(r".*(Renault|Duster|Renault Duster|3)", re.IGNORECASE),                                                         
                }
            },
        "car1":{
            RESPONSE: "Great, you have selected Honda Pilot for how many days you want to book from 1 to 100" .format(), 
            TRANSITIONS: {
                ("car_rental","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            } 
        },
        "car2":{
            RESPONSE: "Great, you have selected Toyota Fortuner for how many days you want to book from 1 to 100" .format(), 
            TRANSITIONS: {
                ("car_rental","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        },
        "car3":{
            RESPONSE: "Great, you have selected Renault Duster for how many days you want to book from 1 to 100" .format(), 
            TRANSITIONS: {
                ("car_rental","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        }

    },
    "sedan":{
        "start":{
            RESPONSE: "Great, we have following Sedan \n 1. Honda Civic   $60/day \n 2. Toyota Corolla   $80/day \n 3. Nissan Altima    $60/day \n Please, enter your selection number" .format(), 
            TRANSITIONS: {
                    ("sedan","car1"): cnd.regexp(r".*(Honda|Civic|Honda Civic|1)", re.IGNORECASE),
                    ("sedan","car2"): cnd.regexp(r".*(Toyota|Corolla|Toyota Corolla|2)", re.IGNORECASE),
                    ("sedan","car3"): cnd.regexp(r".*(Nissan|Altima|Nissan Altima|3)", re.IGNORECASE),                                                         
                }
            },
        "car1":{
            RESPONSE: "Great, you have selected Honda Civic for how many days you want to book from 1 to 100" .format(), 
            TRANSITIONS: {
                ("car_rental","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            } 
        },
        "car2":{
            RESPONSE: "Great, you have selected Toyota Corolla for how many days you want to book from 1 to 100" .format(), 
            TRANSITIONS: {
                ("car_rental","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        },
        "car3":{
            RESPONSE: "Great, you have selected Nissan Altima for how many days you want to book from 1 to 100" .format(), 
            TRANSITIONS: {
                ("car_rental","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        }

    },              
    "road_assistance":{
        "start":{
            RESPONSE: "Welcome, to our Roadside assistance service.\n Please provide your mobile number and address".format(),
            TRANSITIONS: {
                ("road_assistance","book_success"): cnd.true()
            },
        },
        "book_success":{
            RESPONSE: "Thanks for booking with us.Our team will contact you soon." .format(), 
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }             
        },
    },
    "car_service":{
         "start":{
            RESPONSE: "Welcome, to our car maintenance service..\n Please provide your mobile number and address".format(),  
            TRANSITIONS: {
                ("road_assistance","book_success"): cnd.true()
            },          
        },
        "book_success":{
            RESPONSE: "Thanks for booking with us.Our team will contact you soon." .format(), 
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }             
        },
    }
}


actor = Actor(plot, start_label=("global", "start"), fallback_label=("global", "fallback"))
# Skill Personal Transport

## Description

Project idea is to build chatbot for a company which provides following services
1. Car Rental
2. Roadside Assistance
3. Car Service

It uses Dialogflow engine and bert model to identify the intent.
## Quickstart

```bash
pip install -r requirements.txt
```
Run interactive mode
```bash
python run_interactive.py
```

## Example 
type your answer: hi
hi -> Welcome, to our Car service catbot.
 We provide following services
 1. Car Renting
 2. Roadside Assistance
 3. Car service
type your answer: book a car
is_car_service [[47.708527 20.897871 82.171455]]
book a car -> Welcome, to our Rental service.
 What type of car you want to rent SUV, Sedan or Hatchback
type your answer: suv
suv -> Great, we have following SUV
 1. Honda Pilot   $100/day
 2. Toyota Fortuner   $80/day
 3. Renault Duster    $50/day
 Please, enter your selection number
type your answer: 1
1 -> Great, you have selected Honda Pilot for how many days you want to book from 1 to 100
type your answer: 40
40 -> Your booking have been completed.
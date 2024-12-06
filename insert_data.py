from models import Country
from datetime import datetime
from database import SessionLocal

import pandas as pd

db = SessionLocal()

df = pd.read_csv("geoguessr.csv", encoding="cp949")
for i in range(len(df)):
    name =              df.iloc[i]["Country"]
    continent =         df.iloc[i]["Continent"]
    capital =           df.iloc[i]["Capital"]
    domain =            df.iloc[i]["Domain"]
    currency =          df.iloc[i]["Currency"]
    language =          df.iloc[i]["Language"]
    driving_side =      df.iloc[i]["Driving Side"]
    license_plate =     df.iloc[i]["License Plate"]
    bollard =           df.iloc[i]["Bollard"]
    chevron =           df.iloc[i]["Chevron"]
    utility_pole =      df.iloc[i]["Utility Pole"]
    curb =              df.iloc[i]["Curb"]
    guardrail =         df.iloc[i]["Guardrail"]
    lanes =             df.iloc[i]["Lanes"]
    stop_sign =         df.iloc[i]["Stop Sign"]
    pedestrian_sign =   df.iloc[i]["Pedestrian Sign"]
    direction_sign =    df.iloc[i]["Direction Sign"]
    road_number =       df.iloc[i]["Road Number"]
    road_sign =         df.iloc[i]["Road Sign"]
    sign_traffic_post = df.iloc[i]["Sign/Traffic Post"]
    architecture =      df.iloc[i]["Architecture"]
    landscape =         df.iloc[i]["Landscape"]
    google_car =        df.iloc[i]["Google Car"]
    follow_car =        df.iloc[i]["Follow Car"]
    street =            df.iloc[i]["Street"]
    rift =              df.iloc[i]["Rift"]
    camera_gen =        df.iloc[i]["Camera Generation"]
    miscellaneous =     df.iloc[i]["Miscellaneous"]

    #print(name, continent, capital, domain)
    q = Country(
        name=name, 
        continent=continent, 
        capital=capital, 
        domain=domain, 
        currency=currency,
        language=language,
        driving_side=driving_side,
        license_plate=license_plate,
        bollard=bollard,
        chevron=chevron,
        utility_pole=utility_pole,
        curb=curb,
        guardrail=guardrail,
        lanes=lanes,
        stop_sign=stop_sign,
        pedestrian_sign=pedestrian_sign,
        direction_sign=direction_sign,
        road_number=road_number,
        road_sign=road_sign,
        sign_traffic_post=sign_traffic_post,
        architecture=architecture,
        landscape=landscape,
        google_car=google_car,
        follow_car=follow_car,
        street=street,
        rift=rift,
        camera_gen=camera_gen,
        miscellaneous=miscellaneous,
        create_date=datetime.now()
    )

    db.add(q)

db.commit()


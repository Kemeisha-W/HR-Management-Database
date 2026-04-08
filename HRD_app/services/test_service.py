from pathlib import Path
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, LargeBinary
# from sqlalchemy.orm import Session

def insert_images(comp_names):
    img_name = comp_names[0]+".png"
    file_path = BASE_DIR/ "Logos" / img_name
    print("FILE_PATH:",file_path)
    if file_path.exists():
        with open(str(file_path), "rb") as f:
            image_bytes = f.read()
            insert_statement = company.insert().values(
            name= comp_names[1],
            Logo =image_bytes,
            Location = 'Location 1')
        
        #auto-commit on success
        with engine.begin() as conn:
            conn.execute(insert_statement)
        print(comp_names[1]+" inserted successfully.")
    else:
        print("Not Entered")


def display_image(file_path):
    from PIL import Image
    img = Image.open(file_path)
    img.show()

db_path = Path(__file__).resolve().parent / "hr_management.db"
engine = create_engine(f"sqlite:///{db_path}",echo = True)

meta = MetaData()

company = Table(
    "Company",
    meta,
    Column('code',Integer, primary_key=True, nullable=False),
    Column('name',String, nullable=False),
    Column('Logo', LargeBinary),
    Column('Location', String)
)

meta.create_all(engine)
conn = engine.connect()

BASE_DIR = Path(__file__).resolve().parent
compImages = {"CC":["Custom Corp","Custom Corporation"],
              "KF":["KinForm","KinForm"],
              "LLL":["LiveLifeLtd","Live Life Limited"],
              "MM":["Member Mang","Member Management"]}


for k,v in compImages.items():
    print("\n \n KEY:"+k)
    print("\n \n Values:",v)
    insert_images(v)
conn.commit()

#SELECT STATEMENT
# select = company.select().where(company.c.code == 1)
# result = conn.execute(select)
# for row in result:
#     print(row)


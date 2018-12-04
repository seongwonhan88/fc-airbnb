# FastBnB project(Backend)
## Project Detail 
 - Airbnb의 Mock Site로 최대한 비슷하게 구현
 - Front/iOS 별도 구성
 
## Members & Roles  
 - 김태철: 데이터 크롤링(Airbnb API참고), 예약 기능 및 API구현
 - 한성원: 데이터 모델링, API 및 배포 

## Installation
### Requirements 
 - python 3.6  
 `pip install -r requirements.txt`

### Secrets 
   `base.json`  
~~~    
{
   "SECRET_KEY" : "<SECRET_KEY>",
}
~~~

   `production.json`
~~~
{
  "DATABASES": {
    "default": {
      "ENGINE": "<DBENGINE>",
      "HOST": "<HOST>",
      "NAME": "<DBNAME>",
      "USER": "<USER>",
      "PASSWORD": "<USER>",
      "PORT": #PORT
    }
  },
  "AWS_ACCESS_KEY_ID":"<ACCESS_KEY>",
  "AWS_SECRET_ACCESS_KEY":"<ACCESS_SECRET>",
  "AWS_STORAGE_BUCKET_NAME":"<BUCKETNAME>",
  "SENTRY_DSN":"<SENTRY_DSN>"

}
~~~

## Model 
### Home
- Amenity, Booking, BookingDates, HostImages, Room, RoomInfo
### User
- Host, User


## Tools and Third-Party
- Django-Filter
- Django-Cors-Header
- Django REST Framework

## Documentation
- Gitbook: https://fastbnb.gitbook.io/project/

## API TEST
- https://backends.xyz/api/home/listings/
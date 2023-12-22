# Discover & Kickstart Your Business Ideas
<div align="center">
  <img src="https://raw.githubusercontent.com/Biger5/Biger5/main/assets/Screenshot%202023-12-22%20032741.png">
</div>

![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

<p style="text-align: justify">
  Our application, Biger - Discover & Kickstart Your Business, is an application tailored to empower MSMEs by facilitating the exploration of innovative business ideas. Using technologies like machine learning, mobile development, and cloud computing, this application 
  offers a range of optional features to guide users in generating updated and competitive business concepts. Users experiencing challenges in identifying business ideas can use Biger application, which employs advanced algorithms to provide personalized recommendations. 
  Our application goal is to support businesses in staying relevant, sustainable, and responsive to the changing demands of today's market.
</p>

## Machine Learning
This machine learning capability is created using TensorFlow. This service loads the SavedModel and uses the Fast API to serve predictions via the http server.

### Main Page
> URL : https://bs-rec4-awzaea3bwq-et.a.run.app/
- Method
  
  /GET
- Response 

  ```json
  {
    "serverStatus":"server is running...",
    "team":"CH2-PS514",
    "TFversion":"2.15.0"
  }
  ```

### Predict Business Recommendation
> URL : https://bs-rec4-awzaea3bwq-et.a.run.app/v1/business
- Method
  
  /POST
- Request Body

  > **`formattedAddress`** as `string`, **required**, user's location address, the more specific the better
  > 
  > **`price`** as `string`, **required**, the value must be **MODERATE**, **EXPENSIVE**, **INEXPENSIVE**
  > 
  > **`rating`** as `float`, **required**, The rating value is a float number between **0** and **5.0**
  >
- Response 

  ```json
  [
    {
        "price": "MODERATE",
        "longitude": 106.8400393,
        "latitude": -6.1954774,
        "rating": 4.3,
        "kategori": "indonesian_restaurant",
        "Restaurant": "Ampera 2 Tak Restaurant",
        "url": "https://maps.google.com/?cid=12910087911731173234",
        "id": "ChIJRy0T3Dj0aS4RchfNHY7YKbM"
    },
    {
        "price": "MODERATE",
        "longitude": 106.833705,
        "latitude": -6.162701,
        "rating": 4.2,
        "kategori": "restaurant",
        "Restaurant": "Bakmi Gang Kelinci - Pasar baru",
        "url": "https://maps.google.com/?cid=17426949580954964852",
        "id": "ChIJ9SeKMMT1aS4RdJN220_22PE"
    },
    {
        "next": "data"
    }
  ]
  ```

  This prediction returns 10 business recommendations whose preference values best match the user's.

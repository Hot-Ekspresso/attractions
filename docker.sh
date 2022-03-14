docker build -t safinsaf/attractions:1.0 .
docker push safinsaf/attractions:1.0
docker run -p 8000:8000 safinsaf/attractions:1.0
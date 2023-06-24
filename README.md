# commandos de construccion de imagen docker
docker build -t backendecommerce .
docker run --name backendecommercerun -d -p 8000:8000 backendecommerce
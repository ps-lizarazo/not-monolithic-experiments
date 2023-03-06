# not-monolithic-experiments
Entrega para la materia de diseño y construcción de aplicaciones no monolíticas


source wsl-init.sh

flask --app src/ordenes/api run --port=5000
flask --app src/centrodistribucion/api run --port=5001
flask --app src/entregas/api run --port=5002
from flask import Flask, request
from flask_restful import Api, Resource

# Inisialisasi aplikasi Flask
app = Flask(__name__)
api = Api(app)

# data sementara untuk contoh (bisa disesuaikan dengan database atau storage lainnya)
data_store = {
    "username": "Ninym Ralei",
    "email": "ninym.ralei@gmail.com"
}

class Home(Resource):
    def get(self):
        return {"data": data_store}

    def post(self):
        # mengambil data JSON dari request body
        new_data = request.json
        # memperbarui data_store dengan data baru
        data_store.update(new_data)
        return {"pesan": "Data berhasil ditambahkan/diperbarui", "data_baru": data_store}, 201

    def put(self):
        # mengambil data JSON dari request body
        updated_data = request.json
        # memperbarui nilai data jika kunci ada
        for key, value in updated_data.items():
            if key in data_store:
                data_store[key] = value
            else:
                # mengembalikan/menampilkan pesan jika kunci tidak ditemukan
                return {"pesan": f"Kunci '{key}' tidak ditemukan"}, 404
        return {"pesan": "Data berhasil diperbarui", "data_diperbarui": data_store}, 200

    def delete(self):
        data_store.clear()
        return {"pesan": "Data berhasil dihapus"}, 200

# menambahkan resource `Home` ke API
api.add_resource(Home, "/Home")

if __name__ == '__main__':
    # menjalankan aplikasi Flask
    app.run(debug=True)

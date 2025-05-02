# Menggunakan Node.js image
FROM node:16

# Menentukan working directory dalam container
WORKDIR /app

# Menyalin semua file dari folder backend ke dalam container
COPY . .

# Install dependencies
RUN npm install

# Menentukan port yang akan digunakan
EXPOSE 3000

# Menjalankan aplikasi
CMD ["npm", "start"]

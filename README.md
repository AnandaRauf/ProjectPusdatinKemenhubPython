<<<<<<< HEAD
Project Pustadin Kemenhub Python

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Pustadin Kemehub tanggal mulai project 03 Januari 2024

Update Project pada tanggal 04 Januari 2024

Task:
1. Membuat Database untuk Jasa Marga Gerbang dan untuk Jasa  Marga Gerbang Kode Cabang 2  31 dari Desember Sampai Bulan November 2023 dan Show Data di Flask(Selesai)
2. Menampilkan api Jasa Marga Lalu Lintas semua gerbang dijadikan satu tabel(progress)

API JASA MARGA:
https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=2&kode_gerbang=31&tanggal=2023-11-01

curl --location 'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=2&kode_gerbang=31&tanggal=2023-12-29' \
--header 'Authorization: 2628228679' \
--header 'Content-Type: application/json'

curl --location 'https://jid.jasamarga.com/client-api/data/gerbang' \
--header 'Authorization: 2454282048' \
--header 'Content-Type: application/json'

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Cara menggunakan:

1. [Download Python]("https://www.python.org/downloads/")
2. Setting Environtment Variabel Path System dan User: python_patch/Scripts dan python/Scripts/Lib
3. [Download Visual Studio Code]("https://code.visualstudio.com/download")
4. Buka Visual Studio,download extension Python
5. Buka Project di Menu File atau bisa tekan CTRL+K+O
6. Buka Terminal di Visual Studio Code bisa tekan CTRL+SHIFT+'
7. ketik pip install mysql-connector,pip install flask, pip install jinja2
8. Kemudian ketik di terminal Visual Studio Code: py nama_script.py
9. Selesai

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



=======
# V-Dashboard

Dashboard starter template built with Vite, Vue 3, Tailwind CSS and TypeScript.

Copied from https://github.com/tailwindcomponents/dashboard and converted to Vue.

## Demo

https://v-dashboard.vercel.app/

![Demo](https://i.imgur.com/RqXxEHL.gif)

Note if you have access to [Tailwind UI](https://tailwindui.com), you can follow the following steps to add it:

1. Install `@tailwindcss/ui`:

```sh
yarn add @tailwindcss/ui
```

2. Add the plugin in `tailwind.config.js` without changing anything else:

```js
// tailwind.config.js
module.exports = {
  // ...
  // rest of the config
  plugins: [require('@tailwindcss/ui')],
}
```

## Project setup
```
yarn
```

### Compiles and hot-reloads for development
```
yarn dev
```

### Compiles and minifies for production
```
yarn build
```

## License & copyright

Licensed under the [MIT License](LICENSE.md).
>>>>>>> 53fec99 (Website Jasa Marga UI)

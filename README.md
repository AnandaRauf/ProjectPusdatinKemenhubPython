Project Pustadin Kemenhub Python

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Pustadin Kemehub tanggal mulai project 03 Januari 2024

Update Project pada tanggal 04 Januari 2024

Task:
1. Membuat Database untuk Jasa Marga Gerbang dan untuk Jasa  Marga Gerbang Kode Cabang 2  31 dari Desember Sampai Bulan November 2023 dan Show Data di Flask(Selesai)
2. Menampilkan api Jasa Marga Lalu Lintas semua gerbang dijadikan satu tabel(progress)
3. Tarik data api Jasa Marga Gerbang dari tanggal 04 Januari sampai 31(Selesai),Tarik data api Jasa Marga Gerbang Lalin dari tabel Jasa Marga Gerbang dari tanggal 04 Januari sampai 31 dari tanggal 04 Januari sampai 31(Progress),Satukan data semua gerbang ke satu tabel Lalin(Selesai)

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


## License & copyright

Licensed under the [MIT License](LICENSE.md).
>>>>>>> 53fec99 (Website Jasa Marga UI)
=======
# [Admin One &mdash; Free Tailwind Admin Dashboard](https://justboil.me/tailwind-admin-templates)

[![version](https://img.shields.io/github/v/release/justboil/admin-one-tailwind)](https://justboil.me/tailwind-admin-templates)  [![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://justboil.me/tailwind-admin-templates)

[![Free Tailwind CSS admin dashboard](https://justboil.me/images/one-tailwind/repository-preview-hi-res.png)](https://justboil.github.io/admin-one-tailwind/)

**Admin One** is simple, beautiful and free Tailwind CSS admin dashboard

* Free under MIT License
* Built with Tailwind CSS Framework
* Pure HTML & CSS
* No js framework dependencies
* Ready-to-use CSS files
* [Premium Vue.js 3 version](https://justboil.me/tailwind-admin-templates/vue-dashboard) available

## Table of Contents

* [Other versions](#other-versions)
* [Demo](#demo)
* [Quick Start](#quick-start)
* [Browser Support](#browser-support)
* [Reporting Issues](#reporting-issues)
* [Licensing](#licensing)
* [Useful Links](#useful-links)

## Other versions

This is Pure HTML/CSS Tailwind CSS admin dashboard version

<table>
    <tr>
        <td align="center" colspan="2"><a href="https://justboil.me/tailwind-admin-templates"><img src="https://justboil.me/images/tailwind-gh-logo.png?v=2" width="219" height="40" alt="Tailwind CSS admin dashboard templates"></a></td>
    </tr>
    <tr>
        <td align="center"><a href="https://github.com/justboil/admin-one-tailwind" title="Free Tailwind CSS admin dashboard HTML"><img src="https://justboil.me/svg/language-html5.svg" width="64" height="64"></a></td>
        <td align="center"><a href="https://github.com/justboil/admin-one-vue-tailwind" title="Free Vue.js 3 Tailwind CSS admin dashboard"><img src="https://justboil.me/svg/vuejs.svg" width="64" height="64"></a></td>
    </tr>
    <tr>
        <td align="center">Tailwind admin dashboard<br/>Pure HTML/CSS<br/><br/><a href="https://github.com/justboil/admin-one-tailwind" title="Free Tailwind admin dashboard HTML CSS">Free</a></td>
        <td align="center">Tailwind admin dashboard<br/>Vue.js 3<br/><br/><a href="https://github.com/justboil/admin-one-vue-tailwind" title="Free Vue.js 3 Tailwind CSS admin dashboard">Free</a> | <a href="https://justboil.me/tailwind-admin-templates/vue-dashboard" title="Vue.js 3 Tailwind CSS admin dashboard">Premium</a></td>
    </tr>
</table>

## Demo

#### Free dashboard demo

https://justboil.github.io/admin-one-tailwind/

#### Premium Vue.js 3 dashboard demo

https://tailwind-vue.justboil.me/

## Quick Start 

#### Get the repo

* [Create new repo](https://github.com/justboil/admin-one-tailwind/generate) from this template
* &hellip; or clone the repo on GitHub
* &hellip; or [download .zip](https://github.com/justboil/admin-one-tailwind/archive/master.zip) from GitHub

#### HTML & CSS

Check `dist` directory.

#### npm tools

##### Install

`cd` to project's dir and run `npm install` 

##### Build

`npm run build` to rebuild `dist` from sources in `src` directory

## Browser Support

We try to make sure Dashboard works well in the latest versions of all major browsers

<img src="https://justboil.me/images/browsers-svg/chrome.svg" width="64" height="64" alt="Chrome"> <img src="https://justboil.me/images/browsers-svg/firefox.svg" width="64" height="64" alt="Firefox"> <img src="https://justboil.me/images/browsers-svg/edge.svg" width="64" height="64" alt="Edge"> <img src="https://justboil.me/images/browsers-svg/safari.svg" width="64" height="64" alt="Safari"> <img src="https://justboil.me/images/browsers-svg/opera.svg" width="64" height="64" alt="Opera">

## Reporting Issues

JustBoil's free items are limited to community support on GitHub.

The issue list is reserved exclusively for bug reports and feature requests. That means we do not accept usage questions. If you open an issue that does not conform to the requirements, it will be closed.

1. Make sure that you are using the latest version of the Dashboard. Issues for outdated versions are irrelevant
2. Provide steps to reproduce
3. Provide an expected behavior
4. Describe what is actually happening 
5. Platform, Browser & version as some issues may be browser specific

## Licensing

- Copyright &copy; 2019-2021 JustBoil.me (https://justboil.me)
- Licensed under MIT

## Useful Links

- [JustBoil.me](https://justboil.me/)
- [TailwindCSS](https://tailwindcss.com/)
>>>>>>> 50be8c0 (Website Jasa Marga Update UI)

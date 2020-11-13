*[English](README.md), [Türkçe](README.tr.md)*

# Instagram Travel Map
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mysecurityanalytics/insta-travel-map/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/mysecurityanalytics/insta-travel-map.svg?style=social&label=Star&maxAge=2592000)](https://github.com/mysecurityanalytics/insta-travel-map/stargazers/) [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

Bu proje [Çalgan Aygün](https://github.com/calganaygun) tarafından oluşturuldu. Bu projenin amacı bir Instagram kullanıcısının seyahat ettiği rotayı belirlemek ve harita üzerinde göstermektir. Ayrıca bir etiketle etiketlenen gönderilerin harita üzerinden nereden gönderilidğini görebilirsiniz. Program Instagram'dan verileri aktarmak için [instaloader](https://instaloader.github.io/) kullanır.

Web çatısı olarak [Flask](https://flask.palletsprojects.com/en/1.1.x/) kullanıldı. Arayüz geliştirilelerinde [Bootstrap](https://getbootstrap.com/), [Leaflet](https://leafletjs.com/) ve [Leaflet.Heat](https://github.com/Leaflet/Leaflet.heat) kullanıldı .

## Gereklilikler

- Uygulamaya giriş yapmak için bir `Instagram hesabı`.

## Kurulum
> Çok sayıda gönderi ile çalışmak Instagram hesabınızın zaman aşımına uğramasına neden olabilir.
```sh
docker build -t mysa/insta-travel-map .
docker run -d -p 5000:5000 -e INSTA_USERNAME=kullanıcı_adınız -e TAG_MAX_POST=10 mysa/insta-travel-map
docker exec -it <konteyner_id_veya_ismi> instaloader -l <instagram_kullanici_adi>
```
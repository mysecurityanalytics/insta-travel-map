*[English](README.md), [Türkçe](README.tr.md)*

# Instagram Travel Map
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/mysecurityanalytics/insta-travel-map/blob/master/LICENSE) [![GitHub stars](https://img.shields.io/github/stars/mysecurityanalytics/insta-travel-map.svg?style=social&label=Star&maxAge=2592000)](https://github.com/mysecurityanalytics/insta-travel-map/stargazers/) [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


This project is created by [Çalgan Aygün](https://github.com/calganaygun). The aim of the project is to display travel roadmap of a Instagram user on the map, and mark post locations of posted with a tag. In this context, Instagram data were obtained using [instaloader](https://instaloader.github.io/).

[Flask](https://flask.palletsprojects.com/en/1.1.x/) used as a web framework. [Bootstrap](https://getbootstrap.com/), [Leaflet](https://leafletjs.com/) and [Leaflet.Heat](https://github.com/Leaflet/Leaflet.heat) used on the front-end.

## Requirements

- A `Instagram account` to login in app.

## Install
> Working with a large number of posts can cause your Instagram account to get timeout.
```sh
docker build -t mysa/insta-travel-map .
docker run -d -p 5000:5000 -e INSTA_USERNAME=your_username -e TAG_MAX_POST=10 mysa/insta-travel-map
docker exec -it <container_id_or_name> instaloader -l <your_instagram_username>
```
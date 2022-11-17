# Valorant API 
STATUS: https://status.ayberkenis.co

**Built on Henrik's Unofficial API and valo_api**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://choosealicense.com/licenses/mit/) 
[![contributors](https://img.shields.io/github/contributors/ayberkenis/valorant-api?style=for-the-badge)](https://choosealicense.com/licenses/mit/) 
[![contributors](https://img.shields.io/github/issues-pr/ayberkenis/valorant-api?style=for-the-badge)](https://github.com/ayberkenis/valorant-api/pulls)
## API Usage

**Base URL**
```http
https://ayberkenis.co/valorant-api/
```

#### Get Rank


```http
  GET /rank/${username}/${tag}/${region}/$(language)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your Riot Username, ie. Max1ne |
| `tag` | `string` | **Required**. Your Riot Tag, ie. 0000 |
| `region` | `string` | **Optional**. Region, ie. eu |
| `language` | `string` | **Optional**. Language, ie. en |

#### Example Response (Turkish)
```
Rank: Elmas 2 | Güncel RR: 36 | Son Maç: -21 | MMR: 1636
```

____
#### Get Latest Match

```http
  GET /match/${username}/${tag}/${region}/$(language)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :-------------------------------- |
| `username` | `string` | **Required**. Your Riot Username, ie. Max1ne |
| `tag` | `string` | **Required**. Your Riot Tag, ie. 0000 |
| `region` | `string` | **Optional**. Region, ie. eu |
| `language` | `string` | **Optional**. Language, ie. en |


#### Example Response (Turkish)
```
Max1ne son maçını 5 - 13 skoruyla kaybetti. Bu maçtan -21 RR kaybetti. 
Istanbul sunucusunda Icebox haritasında toplam 28 dakika 19 saniye süren maç; 18 round oynandı. 
Oyuncu, maç boyunca toplam 9 kez öldürdü, 15 kez öldü ve 5 kez asist yaptı. 
Rakibe toplam 5 headshot, 27 vücut isabeti yaptı.
```



### Nightbot
Add it to your nightbot by making some changes and using this command below:
Change username and tag to your own credentials.

- `!commands add !rank $(urlfetch https://ayberkenis.co/valorant-api/rank/username/usertag )`
- `!commands add !latestmatch $(urlfetch https://ayberkenis.co/valorant-api/match/username/usertag )`

*For example:*

- `!commands add !rank $(urlfetch https://ayberkenis.co/valorant-api/rank/max1ne/3131 )`
- `!commands add !latestmatch $(urlfetch https://ayberkenis.co/valorant-api/match/max1ne/3131 )`
## How It Looks?

*Match Endpoint:*
![match endpoint](https://i.imgur.com/kJs9kXA.png)

*Rank Endpoint:*
![rank endpoint](https://i.imgur.com/sAVDUcu.png)

## Contributing

Please feel free to contribute on the code itself and help translating API strings to your language. Please read [CONTRIBUTING.md](https://github.com/ayberkenis/valorant-api/blob/master/CONTRIBUTING.md) and proceed for further contribution.



  
## FAQ

#### Can I contribute on the API?

Yes, you can. Please leave Pull Requests, approriate pr's will be accepted and implemented immediately.

#### Is there any rate limiting?

Yes, API is limited to 60 requests per minute. So approx. 1 request per second. That's due to heavy load and also Henrik's Unofficial API did not provide us much larger request pool, this is the max. we could get from them.

#### Do you provide support?

Yes, I'd like to support you if you need help about using the API or with your PR's. [Join my discord](https://discord.gg/sCb9p37YB5)

#### What are the available languages?

We only support Turkish and English for now. But you can help us translating it to your language. Please read [CONTRIBUTING.md](https://github.com/ayberkenis/valorant-api/blob/master/CONTRIBUTING.md) for further support.


## Roadmap

- More optimization
- Adding more endpoints for further assistance
- Building an AI that can analyze last games and make predictions
- Isolate the project from the packages like msgspec, valo_api and making it a standalone API 
- Overwolf Integration


  
## Supporters


- [İlayda Kartal](https://twitch.tv/ilaydakartall)
- [Selin](https://twitch.tv/selinsiiraci)
- [Ivyaxx](https://twitch.tv/ivyaxx)
- [EgoluKayısı](https://twitch.tv/egolukayisi)
- [Quatria](https://twitch.tv/quatria)

  
## Lisans

[MIT](https://choosealicense.com/licenses/mit/)

  
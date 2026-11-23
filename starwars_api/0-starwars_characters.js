#!/usr/bin/node

const request = require('request')

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
	(err, res, body) => {
		if (err) return

		const characters = JSON.parse(body).characters

		const getCharacter = (i) => {
			if (i === characters.length) return

			request(characters[i], (err, res, body) => {
				if (err) return

				console.log(JSON.parse(body).name)
				getCharacter(i + 1)
			})
		}

		getCharacter(0)
	}
)

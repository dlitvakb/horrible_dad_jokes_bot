# Horrible Dad Jokes Bot

This is a [Telegram](https://telegram.org) bot that tells very terrible dad jokes, written for example purposes.

It uses the following services:

* [Contentful](https://www.contentful.com) - For jokes and broadcasted messages storage
* [AWS Lambda](https://aws.amazon.com/lambda/) + [API Gateway](https://aws.amazon.com/api-gateway/) - For hosting the bot and exposing the endpoints
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/) - For storing session data **SOON**

This bot scrapes the interwebs (and pays proper credit to it's creators) for dad jokes. Then allows Telegram users to have some good laughs.

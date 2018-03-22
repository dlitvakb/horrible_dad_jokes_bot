# Horrible Dad Jokes Bot

This is a [Telegram](https://telegram.org) bot that tells very terrible dad jokes, written for example purposes.

It uses the following services:

* [Contentful](https://www.contentful.com) - For jokes and broadcasted messages storage
* [AWS Lambda](https://aws.amazon.com/lambda/) + [API Gateway](https://aws.amazon.com/api-gateway/) - For hosting the bot and exposing the endpoints
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/) - For storing session data **SOON**
* [Serverless](https://serverless.com/) - Managing and automating AWS deploys

This bot scrapes the interwebs (and pays proper credit to it's creators) for dad jokes. Then allows Telegram users to have some good laughs.

### Dependencies

* Node 8+
* Python 3.3+
* Ruby 2.1+ (Optional, for generating your own space)

### Installation & Deploy

* Install `Serverless`:

```bash
npm i -g serverless
```

* Install dependencies on a local folder (for AWS Lambda to use them):

```bash
pip install -r requirements.txt -t vendored
```

* Install `Contentful Bootstrap` for creating your own clone of the Space:

```bash
gem install contentful_bootstrap
```

* Create your space in Contentful:

```bash
contentful_bootstrap create_space "Dad Jokes" -j bootstrap.json
```

> This will also create your account if you don't have one.

* Make a copy of `.env.example` to `.env`

* Copy your Contentful credentials to the `.env` file.

> Space ID and CDA Token are included in the output from Contentful Bootstrap, for CMA Token, you should go to `https://app.contentful.com/spaces/<YOUR_SPACE_ID>/api/cma_tokens` (replace `<YOUR_SPACE_ID>` with your generated Space ID).

* Create your new bot in Telegram by sending the `/newbot` command to [BotFather](https://t.me/botfather) and follow the steps.

* Copy your Bot token to the `.env` file.

* Export your credentials to your terminal session for the `serverless` framework to send them to AWS:

```bash
export $(cat .env | xargs)
```

* Export your AWS credentials for being able to do the AWS deploy:

```bash
serverless config credentials -p aws -k $AWS_ACCESS_KEY_ID -s $AWS_SECRECT_ACCESS_KEY
```

* Deploy your new service:

```bash
serverless deploy
```

* Set up your Telegram hook:

```bash
curl --request POST --url "https://api.telegram.org/bot$TG_BOT_TOKEN/setWebhook" --header 'content-type: application/json' --data '{"url":"<THE_URL_FOR_YOUR_TELEGRAM_ENDPOINT>"}'
```

> Make sure to replace `<THE_URL_FOR_YOUR_ENDPOINT>` with the URL provided by the `serverless deploy` command output.

* Set up your Contentful hook:

Go to `https://app.contentful.com/spaces/<YOUR_SPACE_ID>/settings/webhooks` (replace `<YOUR_SPACE_ID>` with the Space ID in your configuration), and create a webhook indicating your `webhook` endpoint from the `serverless deploy` command as the URL.

> On higher Contentful plans, you can specify which Webhooks to trigger, if you can enable this, set it for `Entry.publish`.

* Enjoy!

### LICENCE

Copyright (c) 2018 David Litvak Bruno - Contentful GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

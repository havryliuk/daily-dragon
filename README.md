# daily-dragon

name: daily-dragon
username: daily_dragon_bot

To deploy with `serverless`:

```serverless deploy --aws-profile havryliuk```

The response will show you the webhook url. Set up a webhook:

```curl --request POST --url https://api.telegram.org/bot<TOKEN>/setWebhook --header 'content-type: application/json' --data '{"url": "https://u3ir5tjcsf.execute-api.us-east-1.amazonaws.com/dev/my-custom-url"}'```

To undeploy:

```serverless remove --aws-profile havryliuk```

Use this article if available:

https://medium.com/hackernoon/serverless-telegram-bot-on-aws-lambda-851204d4236c
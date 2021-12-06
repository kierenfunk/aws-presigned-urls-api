# AWS Bucket Presigned URLs with Serverless Framework

> Generate Presigned urls for AWS buckets using the Serverless Framework

## Usage

### Deployment

```
$ serverless login
$ serverless deploy
```

For more information, refer to [serverless docs](https://www.serverless.com/framework/docs)

### Invocation

After successful deployment, you can call the created application via HTTP:

```bash
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
```

Which should result in response similar to the following:

```json
{
  "url": "...",
  "key": "..."
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function initiator
```

Alternatively, it is also possible to emulate API Gateway and Lambda locally by using `serverless-offline` plugin. In order to do that, execute the following command:

```bash
serverless plugin install -n serverless-offline
```

It will add the `serverless-offline` plugin to `devDependencies` in `package.json` file as well as will add it to `plugins` in `serverless.yml`.

After installation, you can start local emulation with:

```
serverless offline
```

To learn more about the capabilities of `serverless-offline`, please refer to its [GitHub repository](https://github.com/dherault/serverless-offline).

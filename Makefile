publish:
	educates publish-workshop

update: publish
	educates update-workshop

deploy: publish
	educates deploy-workshop

browse:
	educates browse-workshops

git:
	educates publish-workshop . \
  --image=git.gefion.dcai.dk:5050/system-configuration/development/educates/sandbox-demo/workshop \
  --workshop-version=latest 
# lückentext

Macht aus einem deutschen Text einen Lückentext, indem es bestimmtem alle Artikel entfernt. Zur Kontrolle kann man einen beliebigen Artikel in die Lücken einfügen.

Built in python3 on Flask.

Verwendet [deta.sh|deta.sh] als deployment platform, inklusive Deta Base. Dafür braucht man einen Project Key, den man mit einem gratis Account bekommt.

Man kann die Flask app auch problemlos lokal laufen lassen, allerdings benötigt der Zugriff auf deta base einen Internetzugang und den oben erwähnten Project Key.

## commands

```
pip install -r requirements.txt
```

Set deta project key as environment variable:
```
export deta_project_key=<the deta project key>
```

Start:
```
python main.py
```
oder, wenn python3 noch nicht die standard Pythonversion ist:

```
python3 server.py
```
# buildah
See buildah.io

## Build image
```
sudo buildah bud -t lueckentext:0.1 .
```
# Run image
find the container id
```
sudo buildah containers 
```
```
sudo buildah from <container-id>
```
Running by name tries to pull it from a registry.

# podman - much better!

## build
```
podman build -t lueckentext:0.5 .
```

## push to docker
```
podman push localhost/lueckentext:0.6 docker.io/mkugib/lueckentext:0.6
```

## Azure appservice deployment

(https://learn.microsoft.com/en-us/azure/app-service/quickstart-custom-container?tabs=dotnet&pivots=container-windows-cli)

### Create app service plan
https://learn.microsoft.com/en-us/cli/azure/appservice/plan?view=azure-cli-latest#az-appservice-plan-create

```
az appservice plan list --resource-group DefaultResourceGroup-WEU --query "[].{Name:name,Location:location,Kind:kind}" --output table
```

```
az appservice plan create --resource-group DefaultResourceGroup-WEU --location westeurope --sku FREE --name lueckentext-linus --is-linux
``` 
We need a Linux kind.

### create webapp
https://learn.microsoft.com/en-us/cli/azure/appservice/plan?view=azure-cli-latest#az-appservice-plan-create

```
az webapp create --name lueckentext --plan ASP-DefaultResourceGroupWEU-8354 --resource-group DefaultResourceGroup-WEU --deployment-container-image-name mkugib/lueckentext:0.6 
```

check it's there:
```
az webapp list --resource-group DefaultResourceGroup-WEU --query "[].{Name:name,HostNames:hostNames[0],Location:location,Kind:kind,RG:resourceGroup}" --out table
```

```
az webapp list --resource-group DefaultResourceGroup-WEU
```

Example from docs:  
az webapp create --name myContainerApp --plan myAppServicePlan --location eastus --resource-group DefaultResourceGroup-WEU --deployment-container-image-name mcr.microsoft.com/azure-app-service/windows/parkingpage:latest

### update image
```
az webapp config container set --docker-custom-image-name mkugib/lueckentext:0.6 --name lueckentext --resource-group myResoureGroup
```


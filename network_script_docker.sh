#!/bin/bash

sudo docker network create --subnet=172.19.0.0/16 demo_net #Creating a network with the name demo_net

sudo docker container ls | awk '{print $1}' > container_ids # Save the container id's to container_ids

cont_id=$(sed '2!d' container_ids) # take the container_id and storing it in a variable

echo $cont_id

sudo docker network connect --ip 172.19.0.2 demo_net $cont_id #Assigning a static I.P to the container

sudo docker exec -it $cont_id /bin/bash #Enter into the container's bash

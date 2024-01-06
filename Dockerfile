FROM python
RUN python -c 'import os;print(f"Arch: {os.uname().machine}")' > /tmp/arch.txt
WORKDIR /docker_mqtt_1
COPY . /docker_mqtt_1
RUN pip3 install paho-mqtt 

ENTRYPOINT [ "python3","publish.py" ]
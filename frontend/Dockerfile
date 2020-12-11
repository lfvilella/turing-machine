FROM node:15

VOLUME "app/node_modules"

COPY app/package.json /app/

WORKDIR /app

RUN npm install

CMD ["npm", "run", "start"]

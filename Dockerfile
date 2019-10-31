FROM node:lts-alpine

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package.json ./
COPY yarn.lock ./

# install project dependencies leaving out dev dependencies
RUN yarn add --production

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN nuxt build
RUN nuxt start

EXPOSE 8080
CMD [ "http-server", "dist" ]
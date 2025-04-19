# Step 1: Use Node base image
FROM node:18

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy dependency files
COPY package.json package-lock.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the rest of the app
COPY . .

# Step 6: Set OpenSSL legacy flag
ENV NODE_OPTIONS=--openssl-legacy-provider

# Step 7: Build the app
RUN npm run build

# Step 8: Install serve to serve the app
RUN npm install -g serve

# Step 9: Start the app
CMD ["serve", "-s", "dist", "-l", "3000"]

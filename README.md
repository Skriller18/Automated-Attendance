# Automated-Attendance

Use the Automated Attendance System

## Steps to be followed:

Clone this Git Repository
```bash
git clone https://github.com/Skriller18/Automated-Attendance.git
```

Install the needed requirements
```bash
pip install -r requirements.txt
```

Load the images if you have into the faces folder by keeping the name of the image as the name of the label



```bash
npm install
```

## Run the development server locally

To test the app locally, run the backend server in the `indri` repository and then run the frontend server in the `indri-ui` repository.

Make sure to set the `NEXT_PUBLIC_TTS_URL` environment variable to the URL of the backend server. You can copy the `.env.example` file to `.env.local` and set the `NEXT_PUBLIC_TTS_URL` environment variable to the URL of the backend server.

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Deploy on Vercel

1. Run `npm run build`. Make sure the build is successful.
2. Run `vercel --prod`. This will deploy the app on Vercel.

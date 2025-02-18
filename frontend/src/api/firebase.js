// import { initializeApp } from "firebase/app";
// import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";

// // 🔥 Replace with your actual Firebase config
// const firebaseConfig = {
//     apiKey: import.meta.env.VITE_API_KEY,
//     authDomain: import.meta.env.VITE_AUTH_DOMAIN,
//     projectId: import.meta.env.VITE_PROJECT_ID,
//     storageBucket: import.meta.env.VITE_STORAGE_BUCKET,
//     messagingSenderId: import.meta.env.VITE_MESSAGING_SENDER_ID,
//     appId: import.meta.env.VITE_APP_ID
// };
  

// // Initialize Firebase
// const app = initializeApp(firebaseConfig);
// const auth = getAuth(app);
// const googleProvider = new GoogleAuthProvider();

// export { auth, googleProvider, signInWithPopup };
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, RecaptchaVerifier, signInWithPhoneNumber } from "firebase/auth";

// 🔥 Replace with your actual Firebase config
const firebaseConfig = {
    apiKey: import.meta.env.VITE_API_KEY,
    authDomain: import.meta.env.VITE_AUTH_DOMAIN,
    projectId: import.meta.env.VITE_PROJECT_ID,
    storageBucket: import.meta.env.VITE_STORAGE_BUCKET,
    messagingSenderId: import.meta.env.VITE_MESSAGING_SENDER_ID,
    appId: import.meta.env.VITE_APP_ID
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);  // 🔹 Initialize Auth globally
const googleProvider = new GoogleAuthProvider();

export { auth, googleProvider, getAuth, signInWithPopup, RecaptchaVerifier, signInWithPhoneNumber };


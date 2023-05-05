import firebase from 'firebase/app'
import 'firebase/firestore'

const firebaseConfig = {
apiKey: 'AIzaSyBc7wgoR6fFIbAmZl683y6LU_yXHdJMiSY',
authDomain: 'office-supply-store.firebaseapp.com',
projectId: 'office-supply-store',
storageBucket: 'office-supply-store.appspot.com',
messagingSenderId:'449772802376',
appId: '1:449772802376:web:332995cbaabf8d0ad5e37d'
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig)

// access firebase database with db variable
const db = firebase.firestore()

export default db











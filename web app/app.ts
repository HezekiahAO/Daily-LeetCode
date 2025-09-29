import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function LandingPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-6">Welcome to My App</h1>
      <p className="text-lg text-gray-600 mb-8">This is a simple landing page built with React and Tailwind.</p>
      <div className="flex space-x-4">
        <Link to="/next">
          <button className="px-6 py-2 bg-blue-500 text-white rounded-lg shadow hover:bg-blue-600">Go to Next Page</button>
        </Link>
        <button className="px-6 py-2 bg-green-500 text-white rounded-lg shadow hover:bg-green-600">Another Button</button>
        <button className="px-6 py-2 bg-purple-500 text-white rounded-lg shadow hover:bg-purple-600">One More</button>
      </div>
    </div>
  );
}

function NextPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white">
      <h1 className="text-3xl font-semibold mb-4">You are on the Next Page 🚀</h1>
      <Link to="/">
        <button className="px-6 py-2 bg-gray-700 text-white rounded-lg shadow hover:bg-gray-800">Back to Home</button>
      </Link>
    </div>
  );
}

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/next" element={<NextPage />} />
      </Routes>
    </Router>
  );
}

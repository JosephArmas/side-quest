import { useState } from "react";
import  barberShop from "../images/test-barber.jpeg";
import Barbers from "./Barbers";
import Login from "./Login";

export default Nav;
function Nav() {
  const cur_barbers = ["Rj", "John Doe"];
  const [showBarbers, setShowBarbers] = useState(false);
  // const [showLogin, setShowLogin] = useState(false);
  return (
    <div className="nav-conatiner">
      {/* <div className="navbar b-base-100"> */}
      <div className="navbar bg-white">
        <div className="navbar-start">
          <div className="dropdown">
            <label tabIndex={0} className="btn btn-ghost btn-circle">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h16M4 18h7"
                />
              </svg>
            </label>
            <ul
              tabIndex={0}
              className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
            >
              <li>
                <a className="text-lg"onClick={() => setShowBarbers(prevState => !prevState)}>Barbers</a>
                {showBarbers && <Barbers barbers={cur_barbers} />}
              </li>
              <li>
                <a className="text-lg">Services</a>
              </li>
              <li>
                <a className="text-lg">Pricing</a>
              </li>
              <li>
                <a className="text-lg">About</a>
              </li>
            </ul>
          </div>
        </div>
        <div className="navbar-end">
          <button className="login-btn btn btn-ghost btn-circle">Login</button>
          {/* {showLogin && <Login />} */}
          <button className="btn btn-ghost btn-circle">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              />
            </svg>
          </button>
          <button className="btn btn-ghost btn-circle">
            <div className="indicator">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
                />
              </svg>
              <span className="badge badge-xs badge-primary indicator-item"></span>
            </div>
          </button>
        </div>
      </div>
      <div className="barber-pic relative">
        <span className="text-5xl absolute top-1/3 left-1/2 transform -translate-x-1/2 translate-y-1/2 text-white font-bold italic">MadWrist</span>
        <img src={barberShop} alt="barbershop" className="mx-auto"/>
      </div>
    </div>




  );
}

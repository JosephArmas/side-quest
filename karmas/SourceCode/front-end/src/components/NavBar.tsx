import { useState } from "react";
import avatar from "../images/avatar-icon.png";
import { TypeAnimation } from 'react-type-animation'
export default NavBar;

function NavBar() {
  const [isOpen, setIsOpen] = useState(true);
  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <div className="navbar bg-base-100">
        <div className="navbar-start">
          <div className="dropdown dropdown-bottom">
            <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
              <div className="w-10 rounded-full">
                <img src={avatar} />
              </div>
            </label>
            <ul
              tabIndex={0}
              className="menu menu-sm dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52 z-50"
            >
              <li>
                <a className="justify-between">
                  Profile
                  <span className="badge">New</span>
                </a>
              </li>
              <li>
                <a>Settings</a>
              </li>
              <li>
                <a>Logout</a>
              </li>
            </ul>
          </div>
        </div>
        <div className="navbar-center animate-bounce">
          <TypeAnimation
            sequence = {
              ['KARMAS']
            }
            style = {{fontSize: '2rem', fontWeight: 'bold', color: 'white'}}
            speed = {1}
            cursor = {false}
            />
          {/* <a className="btn btn-ghost normal-case text-xl">KARMAS</a> */}
        </div>
        <div className="navbar-end">
          {/* insert cart code */}
          <div className="dropdown dropdown-end">
            <label tabIndex={0} className="btn btn-ghost btn-circle">
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
                    d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                  />
                </svg>
                {isOpen && (
                  <span className="badge badge-sm indicator-item">8</span>
                )}
              </div>
            </label>
            <div
              tabIndex={0}
              className="mt-3 z-40 card card-compact dropdown-content w-52 bg-base-100 shadow"
            >
              <div className="card-body ">
                <span className="font-bold text-lg">8 Items</span>
                <span className="text-info">Subtotal: $999</span>
                <div className="card-actions">
                  <button className="btn btn-primary btn-block">
                    View cart
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="p-3 drawer-end relative z-50">
            <input
              id="my-drawer-4"
              type="checkbox"
              className="drawer-toggle"
              onClick={handleToggle}
            />
            <div className="drawer-content">
              <label
                htmlFor="my-drawer-4"
                tabIndex={0}
                className="btn btn-ghost btn-circle"
              >
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
            </div>
            <div className="drawer-side">
              <label htmlFor="my-drawer-4" className="drawer-overlay"></label>
              <ul className="menu p-4 w-80 h-full bg-base-200 text-base-content">
                <span>CATEGORIES</span>
                <li>
                  <a> ALL ITEMS</a>
                </li>
                <li>
                  <a>SHIRTS</a>
                </li>
                <li>
                  <a>SWEATERS</a>
                </li>
                <li>
                  <a>PANTS</a>
                </li>
                <li>
                  <a>SHORTS</a>
                </li>
                <li>
                  <a>ACCESSORIES</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>




    </>
  );
}

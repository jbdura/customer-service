import Link from 'next/link';

function Navbar () {
    <nav className="bg-gray-800 p-4 text-white fixed w-full top-0 z-10">
      <div className="container mx-auto flex justify-between items-center">
        {/* Brand Logo or Name */ }
        <Link href="/">
          <a className="text-xl font-bold">Home</a>
        </Link>

        {/* Navigation Links */ }
        <ul className="flex space-x-4">
          <li>
            <Link href="/">
              <a className="hover:text-gray-300">Home</a>
            </Link>
          </li>
          <li>
            <Link href="/messages">
              <a className="hover:text-gray-300">Messages</a>
            </Link>
          </li>
          <li>
            <Link href="/customers">
              <a className="hover:text-gray-300">Customers</a>
            </Link>
          </li>
          <li>
            <Link href="/agents">
              <a className="hover:text-gray-300">Agents</a>
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  };

export default Navbar;

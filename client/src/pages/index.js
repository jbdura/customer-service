import Image from 'next/image'
import Link from 'next/link'
import { Inter } from 'next/font/google'

import Navbar from '../components/Navbar'


const inter = Inter({ subsets: ['latin'] })


export default function Home () {
  return (
    <main className="flex items-center justify-center h-screen">
      <div>
        <Navbar />
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl">
        {/* Agents Card */ }
        <Link href="/agents" className="bg-blue-500 text-white p-4 rounded-md cursor-pointer transition transform hover:scale-105 block">
          {/* className="bg-blue-500 text-white p-4 rounded-md cursor-pointer transition transform hover:scale-105 block" */}
            <h2 className="text-lg font-semibold mb-2">Agents</h2>
            <p className="text-sm">View and manage agents</p>
        </Link>

        {/* Customers Card */ }
        <Link href="/customers" className="bg-green-500 text-white p-4 rounded-md cursor-pointer transition transform hover:scale-105 block">
            <h2 className="text-lg font-semibold mb-2">Customers</h2>
            <p className="text-sm">View and manage customers</p>
        </Link>

        {/* Messages Card */ }
        <Link href="/messages" className="bg-purple-500 text-white p-4 rounded-md cursor-pointer transition transform hover:scale-105 block">
            <h2 className="text-lg font-semibold mb-2">Messages</h2>
            <p className="text-sm">View and manage messages</p>
        </Link>
      </div>
    </main>
  );
}


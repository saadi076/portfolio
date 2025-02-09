import React, { useState, useEffect } from "react";
import express from "express";
import cors from "cors";
import bodyParser from "body-parser";

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Server-side API to handle contact form
app.post("/api/contact", (req, res) => {
    const { name, email, message } = req.body;
    if (!name || !email || !message) {
        return res.status(400).json({ error: "All fields are required" });
    }
    console.log("New Contact Message:", { name, email, message });
    res.status(200).json({ success: true, message: "Message sent successfully!" });
});

// Next.js API Route Support
export default function Portfolio() {
    const [typingText, setTypingText] = useState("");
    const text = "Passionate about AI and Machine Learning";

    useEffect(() => {
        let index = 0;
        const interval = setInterval(() => {
            if (index < text.length) {
                setTypingText((prev) => prev + text.charAt(index));
                index++;
            } else {
                clearInterval(interval);
            }
        }, 100);
    }, []);

    return (
        <div className="container mx-auto p-4">
            <nav className="flex justify-between items-center py-4 bg-gray-800 text-white px-6">
                <h1 className="text-xl font-bold">My Portfolio</h1>
                <ul className="flex space-x-4">
                    <li><a href="#about">About</a></li>
                    <li><a href="#skills">Skills</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
            
            <section className="text-center mt-10">
                <h2 className="text-3xl font-bold">Hi, I'm Saad!</h2>
                <p className="text-lg text-gray-600 mt-2">{typingText}</p>
            </section>
            
            <section id="about" className="mt-10">
                <h3 className="text-2xl font-semibold">About Me</h3>
                <p className="text-gray-700">I am a passionate software engineer specialized in AI and Machine Learning.</p>
            </section>
            
            <section id="skills" className="mt-10">
                <h3 className="text-2xl font-semibold">Skills</h3>
                <ul className="list-disc pl-5">
                    <li>Python</li>
                    <li>Machine Learning</li>
                    <li>React & Next.js</li>
                    <li>Flutter</li>
                </ul>
            </section>
            
            <section id="contact" className="mt-10">
                <h3 className="text-2xl font-semibold">Contact Me</h3>
                <form method="POST" action="/api/contact" className="mt-4">
                    <input className="border p-2 w-full" type="text" name="name" placeholder="Your Name" required />
                    <input className="border p-2 w-full mt-2" type="email" name="email" placeholder="Your Email" required />
                    <textarea className="border p-2 w-full mt-2" name="message" placeholder="Your Message" required></textarea>
                    <button className="bg-blue-500 text-white px-4 py-2 mt-2">Send</button>
                </form>
            </section>
        </div>
    );
}

export const config = {
    api: {
        bodyParser: false,
    },
};

app.listen(3001, () => console.log("Server running on port 3001"));

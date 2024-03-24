import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  // Array with it's properties
  const links = [
    {
      href: "https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app",
      title: "Docs",
      description: "Find in-depth information about Next.js features and API."
    },
    {
      href: "https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app",
      title: "Learn",
      description: "Learn about Next.js in an interactive course with quizzes!"
    },
    {
      href: "https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app",
      title: "Templates",
      description: "Explore starter templates for Next.js."
    },
    {
      href: "https://vercel.com/new?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app",
      title: "Deploy",
      description: "Instantly deploy your Next.js site to a shareable URL with Vercel."
    }
  ];

  return (
    // main content of the body with the HTML tag
    <main className={styles.main}>
      {/* another content with the images and the link [This is the React JSX code with HTML like code] */}
      <div className={styles.description}>
        <p>
          Get started by editing&nbsp;
          <code className={styles.code}>src/app/page.js</code>
        </p>
        <div>
          <a 
            href="https://vercel.com?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            By{" "}
            <Image
              src="/vercel.svg"
              alt="Vercel Logo"
              className={styles.vercelLogo}
              width={100}
              height={24}
              priority
            />
          </a>
        </div>
      </div>

      
      {/* Image for the Next JS logo  */}

      <div className={styles.center}>
        <Image
          className={styles.logo}
          src="/next.svg"
          alt="Next.js Logo"
          width={180}
          height={37}
          priority
        />
      </div>

      {/* Render a list of links array in a grid layout using map function to iterate over the links array and */}
      {/* generate a new array of JSX elements */}
      
      <div className={styles.grid}>
        {links.map((link, index) => (
          <a
            key={index}
            href={link.href}
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2>
              {link.title} <span>-&gt;</span>
            </h2>
            <p>{link.description}</p>
          </a>
        ))}
      </div>
    </main>
  );
}
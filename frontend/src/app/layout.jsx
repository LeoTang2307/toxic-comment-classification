import "./global.css"

export const metadata = {
  title: "Toxic Comment Classification",
}

export default function RootLayout({ children }) {
 return (
    <html lang="en">
      <head><link rel="icon" href="/favicon/comments-solid.svg" sizes="any"/></head>
      <body suppressHydrationWarning={true}>{children}</body>
    </html>
  )
}

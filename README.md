# brutey
A simple bruteforcing class that you can use and edit to your bruteforcing needs.

# Documentation
  ## Usage
  You can run the bruteforcer but you'll have to pass in certain values for it to work.
  ```
  import bruteclass
  bruteclass.brute("https://website.com/login", "website login username", "./passlist.txt").start()
  ```
  
  ## Editing the class file to your needs
  1) Open [the bruteforcer class at line 55](https://github.com/iUseYahoo/brutey/blob/main/brutey.py#L55).
  2) If your login request is like mine [view imagine here](https://i.imgur.com/8SzMx5S.png), the standard if statement when it sends the login request will give back that it has found the login when it hasn't, This is because it checks the status code (200). If we have a look at the "Response" tab in the developer tols network viewer, [view my response here](https://i.imgur.com/6b3us7C.png), if yours is like mine then we can add inside the code:
  ```
  if r.status_code == 200 and "Incorrect username and/or password." in r.text:
  ```
  This would allow me in this case to have a successfully working bruteforcer for the login page.
  


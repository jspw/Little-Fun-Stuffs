const randomTime = () => {
  const ms = 1000;
  let time = 0;
  while (time < 5 * ms) {
    time = Math.round(Math.random() * 10 * ms);
  }
  return time;
};

const time = randomTime();

const reloader = () => setTimeout(() => location.reload(), time);

const checkMessage = () => {
  console.log("MHSL :: Checking Messages");
  const element = document.getElementsByClassName("bs bt bu bv bw bx by bz ca");
  if (element.length > 0) {
    window.alert("You have a new message there.");
    reloader();
  } else reloader();
};

checkMessage();

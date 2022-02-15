const faqArea = $("#questions-side-screen");

async function createFAQS() {
  await fetch("data.json")
    .then((response) => response.json())
    .then((data) => {
      const faqInfo = data.rows;
      let count = 1;
      faqInfo.forEach((info) => {
        buildQuestion(info, count);
        count++;
      });
    });
}

function buildQuestion(info, count) {
  faqArea.append(
    `<details><summary>${count}. ${info.title}</summary><p>${info.content}</p></details>`
  );
  faqArea.append("<hr>");
}

// The above function could have been done another way but I felt this was less code for the same outcome.
// The other way would have involved creating two seperate elements giving the title element a event listener
// and setting the toggle method on the second created element to hide and display it when the first element arrow is
// clicked.

createFAQS();

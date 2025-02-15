//The creation of an object that will be later changed to a string by forEach(item =>...) for match() module to work through them

let str = {
    "Email addresses" : ["user@example.com", "firstname.lastname@company.co.uk"],
    "URLs" : ["https://www.example.com", "http://subdomain.example.org/pageLinks"],
    "Phone Numbers" : ["(123) 456-7890", "123-456-7890", "123.456.7890"],
    "Credit card numbers" : ["1234 5678 9012 3456", "1234-5678-9012-3456"],
    "HTML tags" : ["<p>", '<div class="example">', '<img src="image.jpg" alt="description">']
};
//The regular expression patterns for fetching
let emRegex = /[a-zA-Z0-9.]+@[a-zA-Z]+\.com?(\.uk)?/g
let urlRegex = /https?:\/\/[a-zA-Z]+\.example\.[a-zA-Z]+(\/[a-zA-Z]+)?/g
let pnum = /\(?\d{3,}\)?(\s|\.|-)\d{3,}(-|.)\d{4,}/g
let ccn = /\d{4,}(\s|-)\d{4,}(\s|-)\d{4,}(\s|-)\d{4,}/g
let htmlRegex = /<[^>]+>/g
// loop used to start an iteration
for (key in str) {
    console.log(`the matches for ${key} are: \n`);
// forEach(item =>...)} used 
str[key].forEach(item => {
    let matched;
    if (key === "HTML tags") {
        matched = item.match(htmlRegex);
      console.log(matched);
    } else if (key === "Email addresses") {
        matched = item.match(emRegex);
        console.log(matched);
    } else if (key === "URLs") {
        matched = item.match(urlRegex);
        console.log(matched);
    } else if (key === "Phone Numbers") {
        matched = item.match(pnum);
        console.log(matched);
    } else{
        matched = item.match(ccn);
        console.log(matched);
    }
})



}

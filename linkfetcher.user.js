// ==UserScript==
// @name         auzef-dl linkfetcher
// @namespace    https://github.com/wintergew/auzef-dl
// @version      06.2024
// @description  Gets player link from aos system to be used in auzef-dl
// @author       wintergew
// @match        *aos.istanbul.edu.tr/ders-islemleri/ders-materyal/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=edu.tr
// @grant        GM_setClipboard
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    // Create a button and style it
    const button = document.createElement('button');
    button.innerText = 'Extract Links';
    button.style.position = 'fixed';
    button.style.bottom = '20px';
    button.style.left = '20px';
    button.style.zIndex = '1000';
    button.style.padding = '10px 20px';
    button.style.backgroundColor = '#007bff';
    button.style.color = '#fff';
    button.style.border = 'none';
    button.style.borderRadius = '5px';
    button.style.cursor = 'pointer';

    // Append the button to the body
    document.body.appendChild(button);

    // Function to extract and process links
    function extractLinks() {
        // Get the HTML of the page
        const html = document.documentElement.innerHTML;

        // Use regex to find all links
        const regex = /https?:\/\/webcast\.istanbul\.edu\.tr\/Mediasite[0-9]\/Play\/[a-zA-Z0-9]+/g;
        const links = html.match(regex);

        if (links) {
            // Log the links to the console
            console.log('Extracted Links:');
            console.log(links.join(','));

            // Copy the links to the clipboard
            GM_setClipboard(links.join(','));

            alert('Links have been copied to the clipboard!');
        } else {
            alert('No links found.');
        }
    }

    // Add click event to the button
    button.addEventListener('click', extractLinks);
})();
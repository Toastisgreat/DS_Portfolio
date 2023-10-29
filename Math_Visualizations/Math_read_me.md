## Math Visualizations
<p>
Hi!!! These aren't really anything special, these are just cool facts that I found about in math and I wanted to make into pretty pictures for my girlfriend/other friends.
<br>
I think the Prime number circles is the coolest one so far, but they all show off interesting visualization techniques in my opinion.

</p>
<h3>Project Descriptions as of 10/28</h3>
<ul>
  <li>Collatz Graphs</li>
  <ul>
    <li>These are a few colorful graphs that show the distribution of collatz numbers, which are the number of steps it takes for any number to reach 1 given 
    two specific binary operations. </li>
    <li>More information can be found <a url="https://en.wikipedia.org/wiki/Collatz-Conjecture">Here</a></li>
  </ul>
  <li>
    Prime Number Circles
  </li>
  <ul>
    <li>These are NOT graphs. They are interesting visualizations of the distribution of the prime numbers.</li>
    <li>These use datashader to plot about a million points coordinates of numbers</li>
    <li>The coordinates are found using a conversion to polar coordinates for some number x: (increment * sin(x) ,increment * cos(x)), where the increment is 1/n, the number of numbers in the data set being visualized.</li>
  </ul>

</ul>
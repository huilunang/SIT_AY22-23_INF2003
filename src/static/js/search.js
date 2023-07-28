const searchInput = document.getElementById("search-input");
const suggestionsContainer = document.getElementById("suggestions");

searchInput.addEventListener("input", function () {
  const searchQuery = this.value;
  if (searchQuery.length > 0) {
    fetch("/get_suggestions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Request-Identifier": "search-suggestions", // Add a custom identifier header
      },
      body: JSON.stringify({ search_query: searchQuery }),
    })
      .then((response) => response.json())
      .then((data) => {
        suggestionsContainer.innerHTML = "";
        if (data && data.suggested_words.length > 0) {
          data.suggested_words.forEach((word) => {
            const element = document.createElement("li");
            const suggestion = document.createElement("a");
            suggestion.classList.add("dropdown-item");
            suggestion.href = "search?q=" + encodeURIComponent(word);
            suggestion.textContent = word;
            element.appendChild(suggestion);
            suggestionsContainer.appendChild(element);
          });

          // Show the suggestions container if there are results
          suggestionsContainer.style.display = "block";
        } else {
          // Hide the suggestions container if no results found
          suggestionsContainer.style.display = "block";

          const element = document.createElement("li");
          element.classList.add("dropdown-item");
          element.href = "#";
          element.textContent = "No results found.";
          suggestionsContainer.appendChild(element);
        }
      });
  } else {
    // Hide the suggestions container if the search query is too short
    suggestionsContainer.style.display = "none";
  }
});

// Event listener for clicks on the document
document.addEventListener("click", function (event) {
  const isClickInsideSearch = searchInput.contains(event.target);
  const isClickInsideSuggestions = suggestionsContainer.contains(event.target);

  // If the click is outside both the search input and suggestions container, hide the suggestions
  if (!isClickInsideSearch && !isClickInsideSuggestions) {
    suggestionsContainer.style.display = "none";
  }
});

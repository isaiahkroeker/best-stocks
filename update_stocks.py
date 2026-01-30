<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Expert Stock Picks</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-black text-white font-sans min-h-screen">

    <div class="max-w-4xl mx-auto px-4 py-10">
        <header class="text-center mb-12">
            <h1 class="text-4xl font-extrabold bg-gradient-to-r from-green-400 to-blue-500 bg-clip-text text-transparent">
                Expert Leaderboard
            </h1>
            <p class="text-gray-400 mt-2">The best stocks to invest in based on analyst consensus.</p>
        </header>

        <div id="leaderboard" class="space-y-4">
            <p class="text-center text-gray-600">Loading live data...</p>
        </div>
    </div>

    <script>
        async function loadStocks() {
            try {
                // 1. Fetch the data created by your GitHub Action
                const response = await fetch('data.json');
                const stocks = await response.json();
                
                const container = document.getElementById('leaderboard');
                container.innerHTML = ''; // Clear loading text

                stocks.forEach((stock, index) => {
                    // 2. Create the row for each stock
                    const row = `
                        <div class="flex items-center justify-between p-5 bg-gray-900 rounded-xl border border-gray-800 shadow-lg">
                            <div class="flex items-center gap-4">
                                <span class="text-xl font-bold text-gray-700">#${index + 1}</span>
                                <div>
                                    <h2 class="text-xl font-bold text-white">${stock.symbol}</h2>
                                    <p class="text-xs text-green-500 uppercase font-semibold">Expert Pick</p>
                                </div>
                            </div>
                            
                            <div class="text-right">
                                <div class="text-sm text-gray-400">Analyst Confidence</div>
                                <div class="text-lg font-mono text-green-400">${stock.score} Pts</div>
                            </div>
                        </div>
                    `;
                    container.innerHTML += row;
                });
            } catch (error) {
                document.getElementById('leaderboard').innerHTML = 
                    '<p class="text-center text-red-500">Waiting for first data update... check back in 5 mins.</p>';
            }
        }

        loadStocks();
    </script>
</body>
</html>

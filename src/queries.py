# providers by city
SELECT city, COUNT(*) AS providers_count
FROM providers
GROUP BY city
ORDER BY providers_count DESC;

# receivers by city
SELECT city, COUNT(*) AS receivers_count
FROM receivers
GROUP BY city
ORDER BY receivers_count DESC;
Which type of provider contributes the most (by quantity)

#type of providers
SELECT p.type AS provider_type, SUM(f.quantity) AS total_quantity
FROM providers p
JOIN food_listings f ON p.provider_id = f.provider_id
GROUP BY p.type
ORDER BY total_quantity DESC;
Contact info for providers in a given city

#name of providers
SELECT name, contact, address
FROM providers
WHERE city = ?;  -- pass city as parameter
Receivers who have claimed the most (by total quantity)

#who recive the most amount of food
SELECT r.receiver_id, r.name, COUNT(c.claim_id) AS claims_count,
       IFNULL(SUM(f.quantity),0) AS total_quantity
FROM receivers r
LEFT JOIN claims c ON r.receiver_id = c.receiver_id
LEFT JOIN food_listings f ON c.food_id = f.food_id
GROUP BY r.receiver_id, r.name
ORDER BY total_quantity DESC;
Total quantity of food available

#city with the higesht amount of food
SELECT IFNULL(SUM(quantity),0) AS total_available
FROM food_listings
WHERE expiry_date >= DATE('now');  -- only unexpired
City with highest number of food listings

#most common food items
SELECT location AS city, COUNT(*) AS listings_count
FROM food_listings
GROUP BY location
ORDER BY listings_count DESC
LIMIT 1;
Most common food types

#most common food items
SELECT food_type, COUNT(*) AS count, SUM(quantity) AS total_quantity
FROM food_listings
GROUP BY food_type
ORDER BY count DESC;
Claims count per food item

#food count
SELECT f.food_id, f.food_name, COUNT(c.claim_id) AS claims_count
FROM food_listings f
LEFT JOIN claims c ON f.food_id = c.food_id
GROUP BY f.food_id, f.food_name
ORDER BY claims_count DESC;
Provider with highest number of successful (Completed) claims

#most completed claims
SELECT p.provider_id, p.name, COUNT(c.claim_id) AS completed_claims
FROM providers p
JOIN food_listings f ON p.provider_id = f.provider_id
JOIN claims c ON f.food_id = c.food_id
WHERE c.status = 'Completed'
GROUP BY p.provider_id, p.name
ORDER BY completed_claims DESC
LIMIT 1;
Percentage of claims by status

#completed status
SELECT status, COUNT(*) AS count,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM claims), 2) AS pct
FROM claims
GROUP BY status;
Average quantity claimed per receiver (overall)
#most claims
SELECT ROUND(AVG(f.quantity),2) AS avg_quantity_claimed
FROM claims c
JOIN food_listings f ON c.food_id = f.food_id;
Meal type claimed the most

#meal type
SELECT f.meal_type, COUNT(c.claim_id) AS claims_count, SUM(f.quantity) AS total_quantity
FROM food_listings f
LEFT JOIN claims c ON f.food_id = c.food_id
GROUP BY f.meal_type
ORDER BY claims_count DESC;
Total quantity donated by each provider

#who provide the most 
SELECT p.provider_id, p.name, SUM(f.quantity) AS total_donated
FROM providers p
JOIN food_listings f ON p.provider_id = f.provider_id
GROUP BY p.provider_id, p.name
ORDER BY total_donated DESC;
Claims per city (based on food listing location)

#food distriputed location
SELECT f.location AS city, COUNT(c.claim_id) AS claims_count
FROM claims c
JOIN food_listings f ON c.food_id = f.food_id
GROUP BY f.location
ORDER BY claims_count DESC;
Food expiring soon (next 2 days)
#food expering soon
SELECT *
FROM food_listings
WHERE expiry_date <= DATE('now','+2 days')
ORDER BY expiry_date ASC;

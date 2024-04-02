# Write your MySQL query statement below
select tweet_id
from Tweets t
where length(t.content) > 15;

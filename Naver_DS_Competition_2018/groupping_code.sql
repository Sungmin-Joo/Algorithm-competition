SELECT Country.countryName, Age.howOld, Category.categoryName, Merital.marriedQ ,Gender.sex, COUNT(*)
FROM User JOIN Country JOIN Age JOIN Category JOIN Merital JOIN Gender
ON User.ages_id=Age.id AND User.country_id=Country.id AND User.category_id = Category.id AND User.married_id = Merital.id AND User.gender_id = Gender.id
WHERE Gender.sex = 'm' AND Merital.marriedQ ='single'
GROUP BY Category.categoryName 
ORDER BY COUNT(*) DESC 
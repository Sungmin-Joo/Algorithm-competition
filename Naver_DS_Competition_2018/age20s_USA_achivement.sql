SELECT Country.countryName, Age.howOld, Category.categoryName
FROM User JOIN Country JOIN Age JOIN Category 
ON User.ages_id=Age.id AND User.country_id=Country.id AND User.category_id = Category.id 
WHERE Age.howOld>=20 AND Age.howOld<30 AND Country.countryName = 'USA' AND Category.categoryName = 'achievement'
ORDER BY Age.howOld DESC, Country.countryName